#!/bin/bash
set -e
echo "🚨 [NANS-PATCH] Durcissement du Bastion GEMINI_CORE_2.6_PRO"

echo "🗑️ [1/4] Purge ARCHIVES_LEGACY..."
rm -rf ARCHIVES_LEGACY

echo "🔑 [2/4] Neutralisation BORROW_KEY hardcodé..."
sed -i 's/const BORROW_KEY = "ia22-emprunt-2025-zoubirou-secret";/const BORROW_KEY = process.env.BORROW_KEY || ""; \/\/ NANS: Secret migré en env/g' ia22_medical_fastapi_integrated.html

echo "📝 [3/4] Création .env.example..."
cat > .env.example <<EOL
# NANS CORE SECRETS - NE JAMAIS COMMIT
BORROW_KEY=ia22-emprunt-2025-zoubirou-secret
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/TU/URL/ICI
EOL

echo "🛡️ [4/4] Mise à jour .gitignore..."
grep -qxF '.env' .gitignore 2>/dev/null || echo '.env' >> .gitignore

echo "🏁 [NANS-PATCH] TERMINÉ."
echo "👉 SUITE: cp .env.example .env && nano .env"
