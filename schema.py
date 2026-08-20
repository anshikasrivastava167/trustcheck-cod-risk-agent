RISK_SCHEMA = {
    "type": "object",
    "properties": {
        "risk_score": {"type": "integer", "minimum": 0, "maximum": 100},
        "risk_level": {"type": "string", "enum": ["low", "medium", "high"]},
        "reason_code": {"type": "string"},
        "flags": {
            "type": "array",
            "items": {"type": "string"}
        }
    },
    "required": ["risk_score", "risk_level", "reason_code", "flags"],
    "additionalProperties": False
}
