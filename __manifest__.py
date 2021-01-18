{
    "name": "Dynamic Print Access Right",
    "author": "Ngasturi",
    "version": "14.0.1.0.0",
    "website": "https://en.ngasturi.id",
    "summary": "Limit user access to print button with configurable access right",
    "description": """
            
        """,
    "depends": [
        "base",
        "web", 
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/assets.xml",
        "views/view.xml"
    ],
    "qweb": [
        "static/src/xml/template.xml"
    ],
    "license": 'LGPL-3', 
    "installable": True,
}
