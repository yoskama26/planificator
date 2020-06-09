# ====
# MENU
# ====
NAV_MENU_LEFT = [
    {
        "name": "Home",
        "url": "/",
        "icon": "fa-home",
    },
    {
        "name": "Projects",
        "url": "/organisation/project/",
        "icon": "fa-briefcase",
    },
    {
        "name": "Teams",
        "url": "/organisation/",
        "icon": "fa-users",
        "submenu": [
            {
                "name": 'Application team',
                "url": '/organisation/application/',
            },
            {
                "name": 'Collaborator',
                'url': '/organisation/collaborator/',
            },
        ],
    },
]
