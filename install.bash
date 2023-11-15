# shell script for quick setup (Run only once!)
echo "Installing dependencies for the sveltekit client..."
cd client && npm i
echo "Setting up virtual env for API..."
cd ../server && python -m venv env
echo "Installing packages for the Fastapi server..."
pip install -r requirements.txt
echo "Installation complete! Your project is ready to run!"