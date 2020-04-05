# Page-159（9-10）
# Using your latest Restaurant class, store it in a module. Make a separate file that importsRestaurant. Make a
# Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.

# from Chapter_09.wjs_03_9_3_6_summary import Restaurant as R
#
# restaurant = R("Jason", "Beef")
#
# restaurant.describe_restaurant()
# restaurant.open_restaurant()


# Page-159（9-11）
# Start with your work from Exercise 9-8 (page 178). Store the classes User, Privileges and Admin in one module. Create
# a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.


from Chapter_09.wjs_03_9_3_6_summary import Admin
admin = Admin("jason", "wang")
admin.describe_user()
admin.privileges.privileges = [
    "can add post",
    "can delete post",
    "can ban user"
]
admin.privileges.show_privileges()


# Page-159（9-12）
# Store the User class in one module, and store the Privileges and Admin classes in a separate module.In a separate
# file, create an Admin instance and call show_privileges() to show that everything is still working correctly.


from Chapter_09.wjs_03_9_3_6_summary import Admin
admin = Admin("jason", "wang")
admin.describe_user()
admin.privileges.privileges = [
    "can add post",
    "can delete post",
    "can ban user"
]
admin.privileges.show_privileges()












