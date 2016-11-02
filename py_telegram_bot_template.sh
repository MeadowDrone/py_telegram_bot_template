# A monitor script for bot that restarts bot if it crashes. Only for production use.

control_c() {
    kill -9 $PID
    exit
}

trap control_c SIGINT

until python py_telegram_bot_template.py; do
    PID=$!
    echo "'py_telegram_bot_template.py' crashed with exit code $?. Restarting..." >&2
    sleep 1
done