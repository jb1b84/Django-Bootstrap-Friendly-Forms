# Django-Bootstrap-Friendly-Forms

An easy to implement and reusable form template for Django that doesn't break Bootstrap

Django doesn't work well with Bootstrap's forms natively, most especially because of the inability to add the `class="form-control"` attribute to inputs (among other reasons).
I had mixed results with the various available add-ons and stumbled across [Tim Fletcher's gist] (https://gist.github.com/TimFletcher/034e799c19eb763fa859) addressing this need. I grew it from there to include a reusable
form template, support for handling checkboxes separately (I don't use radios, but feel free to implement that) and datepickers (which I think Bootstrap sorely needs). 

##Setup and Examples

Let's assume you have a Django app named *myapp* and for our example we'll use just one model named *Book*. Your structure should look like so:
```
myapp/
	templatetags/
		is_checkbox.py
		project_extras.py
	templates/
		myapp/
			bootstrap_form.html
			*book_form.html
	fields.py
	*models.py
```
Files marked by `*` are provided in the **EXAMPLES** folder and need to be customized to your own app. All other files are ready to go, just place them in your app accordingly. If you have multiple apps, don't
worry about which one you place the templatetags in.

There are two components here (forms and datepicker) that you can choose to use individually, but they play well together when using Django and Bootstrap.

##Bootstrap Forms
The two template tags do most of our work here
*add_attrs.py - Adds the `class="form-control"` attribute to inputs needed by Bootstrap for proper styling
*is_checkbox - Checks if the input is a *checkbox* type so that we can style it differently.

`bootstrap_form.html` is your base reusable template. I have included some error handling but you can tweak as needed. Just include it wherever you would normally print out your form, as in *book_form.html* `{% include 'myapp/bootstrap_form.html'%}`

##Datepicker
We add a new field *BSDateField* which can be used in your models just as you would the regular Django DateField. The only difference is it will add an extra *data-input-type* attribute allowing the datepicker JS to pick it up.
In our example *Book* model, we added `date_published = BSDateField(blank=True, null=True, verbose_name="Date Published")` which will behave as a DateField as far as the database is concerned, but allow you to manipulate the display. 

I have used this with [bootstrap-datepicker] (http://www.eyecon.ro/bootstrap-datepicker) but you can swap in any compatible datepicker JS by changing *fields.py*
```
attrs.update({'data-input-type': 'datepicker'}) #Change to whatever your JS requires for handler
```

##Additional Notes
View my extended write up at [http://jpbrown.info/blog/posts/working-with-django-bootstrap-and-forms/] (http://jpbrown.info/blog/posts/working-with-django-bootstrap-and-forms/) explaining all the ins and outs
