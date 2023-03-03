{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ name }}
{% endblock %}


{% block html %}
This is an <strong>html</strong> message.
<img src='https://www.talab.org/wp-content/uploads/2020/06/2121330839-talab-org.jpg'  width="310" 
     height="310" >
{% endblock %}