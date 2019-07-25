# recipe-hook-api
This API can be used as a back end resource for mobile or desktop clients that need to send REST(GET,POST, PATCH, etc.) requests.

## Test Driven Development-TDD
TDD is when you simply write the test before you write the code.

We can start by create a test.py file, then import the TestCase class that will help us write the assertions.

# Custom User Model
In the core app, we create the models and tests in a dedicated tests folder. Because we won't be serving anything from this app, we no need no views. We'll just hold our database models.

- What we're going to test for is we're going to test that our helper function for our model can create a new user.

So we're going to use the create_user function to create a user
and then we're going to verify that the user has been created as expected.

Notice the first time we would expect this test to fail because we haven't created the feature yet.

As you will see it says `create user missing one required argument username`

* this is because we haven't customized the user model and it's still expecting the standard username field that is required for the Django default user model. *

Then you go ahead and create the user model.

## new user email must be normalized(email domain name)
Make a test case to test for case insensitive domain name.

## add validation - story
Add validation test to ensure that an email field has been provided when the create_user func is called.

## create super user func - story
Test creating a new super user.
