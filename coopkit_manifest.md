# COOPKIT MANIFEST — IA CORE 2.6 / GEMINI_CORE_2.6_PRO
version: 2.6.0
scope: cockpit-ia-core
status: operational

## 1. Identity
id: gemini_core_2_6_pro
label: "GEMINI CORE 2.6 PRO — Capsule Cockpit"
role: cockpit_orchestrator
namespace: ia22.core.cockpit.gemini
integrity: sha256-<to-fill-from-build>

## 2. Modules
- planner: ia22.planner.v3
- executor: ia22.executor.v4
- critic: ia22.critic.v3
- state_manager: ia22.state.v6
- sandbox: ia22.sandbox.secure.v3
- telemetry: ia22.telemetry.zh202.v2
- ui_capsule: ia22.ui.capsule.gemini_2_6
- referral_engine: ia22.referral.v1

## 3. Pipelines

### pipeline: default
description: "Boucle standard cockpit GEMINI 2.6"
steps:
  - planner
  - critic
  - executor
  - state_manager
  - telemetry

### pipeline: safe_sandbox
description: "Exécution confinée, sans accès étendu"
steps:
  - sandbox
  - planner
  - critic
  - executor
  - state_manager
  - telemetry

### pipeline: referral
description: "Délégation vers moteurs externes / autres capsules"
steps:
  - referral_engine
  - planner
  - executor
  - state_manager
  - telemetry

## 4. Invariants
- sovereignty: local-first
- network_policy: restricted
- hallucination_tolerance: low
- traceability: full
- cockpit_mode: enabled
- ui_binding: capsule_html
- event_schema: z-h202.ia

## 5. Interfaces
input:
  - user_query
  - ui_event
  - context_packet
  - system_directive
output:
  - draft_response
  - final_response
  - routing_log
  - telemetry_event

## 6. Security
sandbox: strict
permissions:
  - read: context, config, cache
  - write: response, telemetry
  - deny: arbitrary_external_network
  - allow: curated_endpoints (whitelist-id: gemini_core_2_6)

## 7. Telemetry
events:
  - z-h202.userquery
  - z-h202.routinglog
  - z-h202.agentplan
  - z-h202.ragfetch
  - z-h202.draftresponse
  - z-h202.ethicalcheck
  - z-h202.final_response
  - z-h202.ui_event
  - z-h202.error

## 8. UI Capsule Binding
capsule:
  id: gemini_core_2_6_pro_capsule
  type: html_cockpit
  entrypoint: index-capsule.html
  layout:
    - panel: timeline
    - panel: agent_state
    - panel: logs
    - panel: controls
  theme: orbitronic-ia22
