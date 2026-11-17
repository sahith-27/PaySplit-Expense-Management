# Create your views here.

# render  → used to display an HTML page
# redirect → used to move the user to another URL/page
from django.shortcuts import render, redirect
from django.db.models import Sum

# ExpenseForm is our form created using the Expense model
from .forms import ExpenseForm

# login_required → allows only logged-in users to access a view
from django.contrib.auth.decorators import login_required


# ============================================================
# 1. ADD EXPENSE
# ============================================================

@login_required
def add_expense(request):

    if request.method == 'POST':
        form = ExpenseForm(request.POST)

        if form.is_valid():

            # Create expense but don't save yet
            expense = form.save(commit=False)

            # Attach the expense to the logged-in user
            expense.user = request.user

            # Now save the expense
            expense.save()

            return redirect('expense-list')

    else:
        form = ExpenseForm()

    return render(
        request,
        'expenseapp/add_expense.html',
        {'form': form}
    )

# Import Expense model
from .models import Expense


# ============================================================
# 2. DISPLAY EXPENSES
# ============================================================

# Only logged-in users can access this page
@login_required
def expense_list(request):

    # Get only the expenses belonging to the
    # currently logged-in user
    #
    # request.user = currently logged-in user
    #
    # Example:
    # If Sahith logs in:
    # request.user = Sahith
    #
    # So Django gets only Sahith's expenses.
    expenses = Expense.objects.filter(
        user=request.user
    )

    # Send the expenses to the HTML page
    return render(
        request,
        'expenseapp/expense_list.html',
        {'expenses': expenses}
    )


# ============================================================
# 3. UPDATE EXPENSE
# ============================================================

# Import required functions
from django.shortcuts import render, redirect, get_object_or_404

# Import Expense model
from .models import Expense

# Import ExpenseForm
from .forms import ExpenseForm


def update_expense(request, id):

    # Find the expense using its ID
    #
    # Example:
    # /update/5/
    # id = 5
    #
    # If expense with ID 5 exists → get that expense
    # If it does not exist → show 404 error
    expense = get_object_or_404(
        Expense,
        id=id
    )

    # Check whether the user submitted the update form
    if request.method == 'POST':

        # Put the new data into the existing expense
        #
        # instance=expense means:
        # "Update this existing expense"
        form = ExpenseForm(
            request.POST,
            instance=expense
        )

        # Check whether the new data is valid
        if form.is_valid():

            # Don't save immediately
            # First create the updated expense object
            expense = form.save(commit=False)

            # Attach the logged-in user to the expense
            expense.user = request.user

            # Now save the updated expense into the database
            expense.save()

            # After updating, go to expense list
            return redirect('expense-list')

    else:

        # If the page is opened normally,
        # display the existing expense data in the form
        form = ExpenseForm(
            instance=expense
        )

    # Display the Update Expense page
    return render(
        request,
        'expenseapp/update_expense.html',
        {'form': form}
    )


# ============================================================
# 4. DELETE EXPENSE
# ============================================================

def delete_expense(request, id):

    # Find the expense using its ID
    expense = get_object_or_404(
        Expense,
        id=id
    )

    # Delete the expense from the database
    expense.delete()

    # After deleting, go back to expense list
    return redirect('expense-list')


# ============================================================
# 5. REGISTER USER
# ============================================================

# Django's built-in registration form
# It provides username, password and password confirmation
from django.contrib.auth.forms import UserCreationForm


def register(request):

    # Check whether the user submitted the registration form
    if request.method == 'POST':

        # Get the username and password entered by the user
        form = UserCreationForm(request.POST)

        # Check whether the registration details are valid
        if form.is_valid():

            # Create the user account in the database
            form.save()

            # After registration, go to login page
            return redirect('login')

    else:

        # If the page is opened normally,
        # create an empty registration form
        form = UserCreationForm()

    # Display the Register page
    # Send the form to the HTML page
    return render(
        request,
        'expenseapp/register.html',
        {'form': form}
    )


# ============================================================
# 6. LOGOUT USER
# ============================================================

# Django's logout function
from django.contrib.auth import logout

def user_logout(request):

    # Logout the currently logged-in user
    logout(request)

    # After logout, send the user to the login page
    return redirect('login')



from django.contrib.auth import authenticate, login


def user_login(request):

    # Check whether the login form was submitted
    if request.method == 'POST':

        # Get username from the form
        username = request.POST['username']

        # Get password from the form
        password = request.POST['password']

        # Check username and password
        user = authenticate(
            username=username,
            password=password
        )

        # If username and password are correct
        if user is not None:

            # Login the user
            login(request, user)

            # After login, go to expense list
            return redirect('expense-list')

        # If username or password is wrong
        else:

            return render(
                request,
                'expenseapp/login.html',
                {'error': 'Invalid username or password'}
            )

    # Show login page
    return render(
        request,
        'expenseapp/login.html'
    )

from django.db.models import Sum
from django.contrib.auth.decorators import login_required

@login_required
def expense_list(request):

    # Get the logged-in user's expenses
    expenses = Expense.objects.filter(user=request.user)

    # Get the month selected by the user
    selected_month = request.GET.get('month')

    # If the user selected a month
    if selected_month:

        # Example:
        # selected_month = "2026-09"

        year, month = selected_month.split('-')

        # Get expenses only from selected year and month
        expenses = expenses.filter(
            date__year=year,
            date__month=month
        )

    # Calculate total expenses
    total = expenses.aggregate(
        Sum('amount')
    )['amount__sum'] or 0


    # Calculate amount per person
    for expense in expenses:

        if expense.is_shared and expense.shared_people > 0:

            # Example: ₹1000 / 2 = ₹500
            expense.amount_per_person = (
                expense.amount / expense.shared_people
            )

        else:

            # If not shared, full amount
            expense.amount_per_person = expense.amount


    # Calculate amount owed
    for expense in expenses:

        if expense.is_shared and expense.shared_people > 0:

            # Amount owed = amount divided by people
            expense.amount_owed = (
                expense.amount / expense.shared_people
            )

        else:

            # If not shared, user owes full amount
            expense.amount_owed = expense.amount


    # Finally send everything to the HTML page
    return render(
        request,
        'expenseapp/expense_list.html',
        {
            'expenses': expenses,
            'total': total,
            'selected_month': selected_month
        }
    )

from django.db.models import Sum
@login_required
def dashboard(request):

    # Get only the logged-in user's expenses
    expenses = Expense.objects.filter(user=request.user)

    # Calculate total expenses
    total = expenses.aggregate(
        Sum('amount')
    )['amount__sum'] or 0

    # Calculate shared expenses
    shared_total = expenses.filter(
        is_shared=True
    ).aggregate(
        Sum('amount')
    )['amount__sum'] or 0

    # Calculate amount owed
    owed_total = 0

    for expense in expenses:

        if expense.is_shared and expense.shared_people > 0:
            owed_total += (
                expense.amount / expense.shared_people
            )
        else:
            owed_total += expense.amount

    # For now, use total as the monthly value
    # We will improve monthly calculation next
    monthly_total = total

    return render(
        request,
        'expenseapp/dashboard.html',
        {
            'total': total,
            'monthly_total': monthly_total,
            'shared_total': shared_total,
            'owed_total': owed_total
        }
    )
def home(request):

    return render(
        request,
        'expenseapp/home.html'
    )