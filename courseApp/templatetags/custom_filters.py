from django import template

register = template.Library()

# Example 1: Uppercase filter
@register.filter(name='upper_case')
def upper_case(value):
    """Converts a string to uppercase."""
    return value.upper()

# Example 2: Shorten description
@register.filter(name='shorten')
def shorten(value, length=50):
    """Trims text to a given length with ellipsis."""
    if len(value) > length:
        return value[:length] + "..."
    return value

# Example 3: Credits badge
@register.filter(name='credits_badge')
def credits_badge(value):
    """Returns a Bootstrap badge based on credits."""
    if value >= 10:
        return f'<span class="badge bg-success">{value} credits</span>'
    elif value >= 5:
        return f'<span class="badge bg-warning">{value} credits</span>'
    else:
        return f'<span class="badge bg-danger">{value} credits</span>'
