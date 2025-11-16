from core.session_service import InMemorySessionService
from core.memory_bank import MemoryBank
from orchestrator import DisasterOrchestrator
import pprint

session_service = InMemorySessionService()
memory_bank = MemoryBank()
orch = DisasterOrchestrator(session_service, memory_bank)

text = "My father is having chest pain and can't breathe properly."
res = orch.handle_request("user123", "Kadri Mangalore", text)

pprint.pprint(res)
