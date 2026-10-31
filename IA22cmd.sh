#!/bin/bash

GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}===============================================${NC}"
echo -e "${GREEN}  SCRIPT DE RECHERCHE DE COMMANDES D'IA (IA22)  ${NC}"
echo -e "${GREEN}===============================================${NC}\n"

echo -e "${GREEN}--- Recherche de commandes pertinentes dans le PATH ---${NC}"
for dir in $(echo $PATH | sed 's/:/ /g'); do
    find "$dir" -maxdepth 1 -type f -executable \( -name "*ai*" -o -name "*ml*" -o -name "*tf*" -o -name "*torch*" -o -name "*keras*" -o -name "*gpt*" \) 2>/dev/null
done
echo ""

echo -e "${GREEN}--- Vérification des alias liés à l'IA ---${NC}"
alias | grep -i -E 'ai|ml|tensorflow|pytorch|gpt'
echo ""

echo -e "${GREEN}--- Recherche de packages d'IA installés ---${NC}"
if command -v dpkg &> /dev/null; then
    echo "Paquets Debian/Ubuntu :"
    dpkg -l | grep -i -E 'ai|ml|tensorflow|pytorch|keras|gpt' | awk '{print $2}'
fi
if command -v brew &> /dev/null; then
    echo "Paquets Homebrew :"
    brew list | grep -i -E 'ai|ml|tensorflow|pytorch|keras|gpt'
fi
echo ""

echo -e "${GREEN}--- Recherche terminée ---${NC}"
echo "Note : Cette liste peut inclure des commandes non directement liées à l'IA."
echo "Veuillez vérifier manuellement la fonction de chaque commande avec 'man <commande>' ou '<commande> --help'."
