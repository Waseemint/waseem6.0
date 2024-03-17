{% extends "base.html" %}
{% load widget_tweaks %}
{% block content %}

    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}

        <p>Quantity: <input type="number" style="visibility: hidden;" id="id_quantity" name="quantity" value="0" min="0"></p>
        <p>Total Price: <span id="total-price">0</span></p>
        <p>Tax: <span id="tax">0</span></p>
        <p>Total Amount with Tax: <span id="total-amount-with-tax">0</span></p>
        <button type="submit">Place Order</button>
    </form>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script>


$(document).ready(function() {
    $('#id_quantity').val(0);

    $('#id_quantity').change(function() {
        var quantity = $(this).val();
        var productId = "{{ product.id }}";
        $.ajax({
            url: "{% url 'calculate_total_price' %}",
            data: {
                'product_id': productId,
                'quantity': quantity
            },
            dataType: 'json',
            success: function(data) {
                $('#total-price').text(data.total_price);
                $('#tax').text(data.tax);
                $('#total-amount-with-tax').text(data.total_amount_with_tax);
            }
        });
    });

    $('form').submit(function(e) {
        var quantity = $('#id_quantity').val();
        if (quantity <= 0) {
            alert('Quantity must be 1 or greater.');
            e.preventDefault(); 
        }
    });
});




</script>



{% endblock content %}