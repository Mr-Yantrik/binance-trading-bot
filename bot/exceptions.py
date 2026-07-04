"""Custom exception hierarchy for the trading bot."""


class BotError(Exception):
    """Base exception for all bot errors."""


class ConfigError(BotError):
    """Raised when configuration is invalid or missing."""


class ValidationError(BotError):
    """Raised when user input fails validation."""


class OrderExecutionError(BotError):
    """Raised when an order fails to execute on the exchange."""


class ClientConnectionError(BotError):
    """Raised when the exchange client cannot be initialized or reached."""
