inventory_management/
│
├── .gitignore
├── README.md
├── requirements.txt
├── setup.py
├── LICENSE
├── .env
├── .pylintrc
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   └── logging.conf
│
├── data/
│   ├── __init__.py
│   ├── database.py
│   └── migrations/
│       └── (archivos de migración)
│
├── docs/
│   ├── __init__.py
│   ├── architecture.md
│   ├── api_docs.md
│   └── user_guide.md
│
├── inventory_management/
│   ├── __init__.py
│   ├── app.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── inventory.py
│   │   └── user.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── inventory.py
│   │   └── user.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── inventory_service.py
│   │   └── user_service.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── validators.py
│   │   └── helpers.py
│   └── templates/
│       └── (archivos HTML)
│
├── tests/
│   ├── __init__.py
│   ├── test_inventory.py
│   ├── test_user.py
│   └── (otros archivos de prueba)
│
└── scripts/
    ├── __init__.py
    ├── run_server.py
    └── initialize_db.py
