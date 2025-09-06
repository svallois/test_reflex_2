import reflex as rx

config = rx.Config(
    app_name="test_reflex_2",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)