"""
Authentication configuration settings.

This module contains configuration variables for the authentication service,
including token expiration times, security settings, and other authentication
parameters.
"""

# Token expiration time in seconds (2 hours)
TOKEN_EXPIRATION = 7200

# Secret key for JWT token signing (should be set via environment variable in production)
SECRET_KEY = "default-secret-key-change-in-production"

# Algorithm for JWT token encoding
ALGORITHM = "HS256"

# Refresh token expiration time in seconds (7 days)
REFRESH_TOKEN_EXPIRATION = 604800

# Password hashing rounds
BCRYPT_ROUNDS = 12

# Allowed token types
TOKEN_TYPES = ["access", "refresh"]

# Maximum login attempts before account lockout
MAX_LOGIN_ATTEMPTS = 5

# Account lockout duration in seconds (15 minutes)
LOCKOUT_DURATION = 900