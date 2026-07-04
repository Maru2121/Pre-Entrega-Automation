Reporte de Cobertura de Pruebas (Pytest Execution Summary)
Resumen de Ejecución General
Plataforma: Windows 10

Entorno de Ejecución: Python 3.13.0, pytest-9.0.3, pluggy-1.6.0

Plugins Activos: Faker-40.28.1, html-4.2.0, metadata-3.1.1

Resultado Global: 29 passed in 256.54s (0:04:16)

Desglose de Casos de Prueba
Módulo / Archivo	Caso de Prueba (TC)	Tipo de Prueba	Estado
test/api/test_delete_user.py	test_delete_user (API-003)	API (DELETE)	PASSED
test/api/test_get_users.py	test_get_users_list (API-001)	API (GET)	PASSED
test/api/test_post_user.py	test_create_user (API-002)	API (POST)	PASSED
test/test_cart.py	test_add_product_cart	UI (Selenium)	PASSED
test/test_cart.py	test_view_cart	UI (Selenium)	PASSED
test/test_cart.py	test_remove_product	UI (Selenium)	PASSED
test/test_checkout.py	test_checkout_complete	UI (Selenium)	PASSED
test/test_inventory.py	test_inventory_title	UI (Selenium)	PASSED
test/test_inventory.py	test_productos_visibles	UI (Selenium)	PASSED
test/test_inventory.py	test_ui_elements	UI (Selenium)	PASSED
test/test_inventory.py	test_footer_redes	UI (Selenium)	PASSED
test/test_inventory.py	test_imagenes_productos	UI (Selenium)	PASSED
test/test_inventory.py	test_detalle_producto	UI (Selenium)	PASSED
test/test_login.py	test_login_multiples_usuarios[standard_user]	UI (Parametrizada)	PASSED
test/test_login.py	test_login_multiples_usuarios[locked_out_user]	UI (Parametrizada)	PASSED
test/test_login.py	test_login_multiples_usuarios[problem_user]	UI (Parametrizada)	PASSED
test/test_login.py	test_login_multiples_usuarios[performance_glitch]	UI (Parametrizada)	PASSED
test/test_login.py	test_login_multiples_usuarios[error_user]	UI (Parametrizada)	PASSED
test/test_login.py	test_login_multiples_usuarios[visual_user]	UI (Parametrizada)	PASSED
test/test_logout.py	test_logout	UI (Selenium)	PASSED
test/test_product_detail.py	test_product_detail	UI (Selenium)	PASSED
test/test_sorting.py	test_sort_az	UI (Filtros)	PASSED
test/test_sorting.py	test_sort_za	UI (Filtros)	PASSED
test/test_sorting.py	test_sort_low_high	UI (Filtros)	PASSED
test/test_sorting.py	test_sort_high_low	UI (Filtros)	PASSED
test/test_special_users.py	test_performance_user	UI (Selenium)	PASSED
test/test_special_users.py	test_visual_user	UI (Selenium)	PASSED
test/test_special_users.py	test_error_user	UI (Selenium)	PASSED
test/test_special_users.py	test_problem_user	UI (Selenium)	PASSED
Evidencias de Salida Generadas
Los entregables correspondientes a los reportes automáticos se encuentran ubicados localmente en las siguientes rutas dentro del espacio de trabajo:

📁 Reporte HTML Interactivo: reports/report_20260704_003251.html

📁 Reporte de Matriz Excel: reports/results_20260704_003703.xlsx

📁 Trazabilidad y Logs: logs/automation.log