# exercises/m002_class_instance/utils.py
"""Utility functions for shopping system"""

def format_price(price: int) -> str:
    """Format price as currency"""
    return f"${price:,}"

def validate_quantity(qty: int) -> bool:
    """Validate if quantity is positive"""
    return qty > 0

def calculate_discount(price: int, discount_percent: float) -> int:
    """Calculate discounted price"""
    return int(price * (1 - discount_percent / 100))