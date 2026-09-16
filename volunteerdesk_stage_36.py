# === Stage 36: Add templates for quickly creating common records ===
# Project: VolunteerDesk
def create_record_from_template(template_type, **kwargs):
    """Factory: build a common record from its template type and optional overrides.
    
    Supported templates:
      - 'shift': creates a Shift with default duration 4h, status 'scheduled'.
      - 'signup': creates a SignUp with default status 'confirmed'.
      - 'hour_log': creates an HourLog with default notes ''.
      - 'thank_you': creates a ThankYouNote with default message 'Thanks for your service!'.
    
    Use: record = create_record_from_template('shift', volunteer_id=123, start='2025-01-01')
    """
    templates = {
        'shift': {
            'class': 'Shift',
            'defaults': {'duration': 4, 'status': 'scheduled'},
        },
        'signup': {
            'class': 'SignUp',
            'defaults': {'status': 'confirmed'},
        },
        'hour_log': {
            'class': 'HourLog',
            'defaults': {'notes': ''},
        },
        'thank_you': {
            'class': 'ThankYouNote',
            'defaults': {'message': 'Thanks for your service!'},
        },
    }
    
    if template_type not in templates:
        raise ValueError(f"Unknown template: {template_type}. Choose from {list(templates.keys())}.")
    
    tmpl = templates[template_type]
    defaults = {k: v for k, v in tmpl['defaults'].items() if k not in kwargs}
    defaults.update(kwargs)
    
    return tmpl['class'](**defaults)
