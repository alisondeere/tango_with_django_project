<!DOCTYPE html>
<html>
    <head>
        <title>Rango</title>
    </head>

    <body>
        <h1>Add a Category</h1>
        <div>
            <form id="category_form" method="post" action="/rango/add_category/">
                {% csrf_token %}
                {% for hidden in form.hidden_fields %}
                    {{ hidden }}
                {% endfor %}
                {% for field in form.visible_fields %}
                    {{ field.errors }}
                    {{ field.help_text }}
                    {{ field }}
                {% endfor %}
                <input type="submit" name="submit" value="Create Category" />
            </form>
        </div>
    </body>
</html>
                    
