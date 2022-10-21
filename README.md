# Limit the odoo print button with configurable access right

## With this module you can limit the odoo print button with 4 configurable access right

Sign in as Administrator then enter to debug mode. Select Settings >> Technical >> Reporting >> Print Access Right menu.

Create a new record. Give the access right name, then select the report that you want to give the access right. 

Select the type of access right. Select list of user that you want this access right will take an effect. Then set the error message to the affected user.

This is 4 type of access right that you can choose.

### Fixed

![Create fixed print access right](https://en.ngasturi.id/wp-content/uploads/2021/01/odoo_create_fixed_print_right.png)

It's mean the user can not print the document forever. If affected user try to print the related document, an error message will appear.

![Fixed print access right error message](https://en.ngasturi.id/wp-content/uploads/2021/01/odoo_fixed_print_access_right_message.png)



### Fixed Print Count

![Create fixed print count print access right](https://en.ngasturi.id/wp-content/uploads/2021/01/odoo_create_fixed_count_print_right.png)

User can print the document for limited count only. If affected user try to print the related document more than Max Print Count, an error message will appear.

![Fixed print count error message](https://en.ngasturi.id/wp-content/uploads/2021/01/odoo_fixed_print_count_error_message.png)

You can monitor how many times user already print some document in Print Count tab in Settings >> Technical >> Reports menu.

![Monitor the print count](https://en.ngasturi.id/wp-content/uploads/2021/01/odoo_monitor_print_count.png)

### By Condition

![Create by condition print access right](https://en.ngasturi.id/wp-content/uploads/2021/01/odoo_create_by_condition_print_right.png)

![Create by condition print access right domain](https://en.ngasturi.id/wp-content/uploads/2021/01/odoo_create_by_condition_print_right_domain.png)

User can print the document only if the limitation condition not match. You can configure the condition dynamically by creating a domain. If affected user try to print the related document, and the record or data is match with the condition, an error message will appear.

![By condition error message](https://en.ngasturi.id/wp-content/uploads/2021/01/odoo_by_condition_error_message.png)

### By Condition and Print Count

User can print the document only if the limitation condition not match and the print count not reached the Max Print Count.

![Create by condition and print count print access right](https://en.ngasturi.id/wp-content/uploads/2021/01/odoo_create_by_condition_and_print_count.png)


This module is tested in odoo 15, for other versions please check other branches. Please report me if you found a bug.

