# 1️⃣ Deactivate virtual environment if active
deactivate -ErrorAction SilentlyContinue

# 2️⃣ Delete old virtual environment
if (Test-Path ".venv") {
    Write-Host "Deleting old virtual environment..."
    Remove-Item -Recurse -Force .venv
}

# 3️⃣ Remove all .pyc and __pycache__ files in project
Write-Host "Cleaning old compiled Python files..."
Get-ChildItem -Path . -Include *.pyc -Recurse | Remove-Item -Force -ErrorAction SilentlyContinue
Get-ChildItem -Path . -Include __pycache__ -Recurse | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue

# 4️⃣ Create a fresh virtual environment
Write-Host "Creating new virtual environment..."
python -m venv .venv

# 5️⃣ Activate the virtual environment
Write-Host "Activating virtual environment..."
.\.venv\Scripts\Activate.ps1

# 6️⃣ Upgrade pip
Write-Host "Upgrading pip..."
python -m pip install --upgrade pip

# 7️⃣ Install Django, mysqlclient, and PyMySQL
Write-Host "Installing Django, mysqlclient 2.2.8, and PyMySQL..."
pip install --no-cache-dir Django mysqlclient==2.2.8 pymysql

# 8️⃣ Optional: patch PyMySQL for Django
$init_file = ".\courseproject\__init__.py"
if (!(Test-Path $init_file)) {
    New-Item -ItemType File -Path $init_file -Force
}
Add-Content $init_file "`nimport pymysql`npymysql.install_as_MySQLdb()"

# 9️⃣ Verify mysqlclient version
Write-Host "Verifying mysqlclient version..."
python -c "import pkg_resources; print('mysqlclient version:', pkg_resources.get_distribution('mysqlclient').version)"

# 🔟 Run Django migrations
Write-Host "Running Django migrations..."
python manage.py migrate

Write-Host "`n✅ Environment setup complete! Django should now see mysqlclient 2.2.8 correctly."