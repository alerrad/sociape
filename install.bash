# shell script for quick setup
echo "Installing dependencies for the sveltekit client..."
cd client && npm i
cd ..
echo "Installing packages for the Fastapi server..."
cd server && pip install -r requirements.txt
echo "Installation complete! Your project is ready to run!"