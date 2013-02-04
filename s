#Notes:
Here is an example todo list. Everything above the "Todo:" will be ignored, as t only starts parsing after the "#Todo<colon>" keyword.

Entries are started with a tab, then a number indicative of priority, and then the task.
Lines following a task starting with two tabs are considered notes part of the former task

Output of example:
> $ t
>	 Buy groceries
>		Eggs
>		Egg beater
>		Chicken
>
>	 Do laundry
>
>	 Eat brinner
>
>	 Take a nap
>		20 minutes!
>
>	 Finish email to John



#Today:
	0 Finish email to John

	2 Do laundry
	3 Buy groceries
		Eggs
		Egg beater
		Chicken

	1 Take a nap
		20 minutes!
	2 Eat brinner

