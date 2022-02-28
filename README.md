# Reproducing issue

1. docker-compose up -d
2. conda create -n fsissue python=3.8
3. conda activate fsissue
4. pip install -r requirements.txt
5. feast apply
6. python examples/house_test.py