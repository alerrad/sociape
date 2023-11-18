# shell script for running both client & server
echo 'Starting both client & API...'
echo 'Press Ctrl+C to stop'

run_client() {
    cd client && npm run dev
}

run_api() {
    cd server && source ./env/Scripts/activate
    python main.py
}

run_client &
run_api &