train-nlu:
	python3 -m rasa_nlu.train -c nlu_config.yml --fixed_model_name current --data data/intents/ -o models --project nlu --verbose

train-core:
	python3 train.py

train: train-nlu train-core

run-actions:
	python3 -m rasa_core_sdk.endpoint --actions actions.actions

run-rocketchat:
	python3 run-rocketchat.py

run-rest:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/current --debug --port 5005 -c rest

run-console:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/current --debug --endpoints endpoints.yml

train-online:
	python3 -m rasa_core.train -u models/nlu/current/ --online --core models/dialogue/

evaluate:
	python3 -m rasa_core.evaluate -d models/dialogue -s data/core/

