from django import template
from django.contrib.auth.models import User
from django.utils.html import format_html

register = template.Library()


@register.filter
def author_details(author: User, current_user: User = None) -> str:
    if author == current_user:
        return format_html("<strong>me</strong>")

    prefix = format_html('<a href="mailto:{}">', author.email) if author.email else ""
    name = (
        f"{author.first_name} {author.last_name}"
        if author.first_name and author.last_name
        else f"{author.username}"
    )
    suffix = format_html("</a>") if author.email else ""

    return format_html("{}{}{}", prefix, name, suffix)
