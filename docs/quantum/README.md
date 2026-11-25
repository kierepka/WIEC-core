# Quantum knowledge and hybrid computing track

Status: research/design track; **no quantum backend is implemented or connected**.
The classical core must work without a quantum SDK, account or device.

## Why quantum belongs here

WIEC is intended to compare independent computational perspectives and retain
their evidence. A quantum method may become one specialized contributor where
the problem and measured results justify it. The scientific question is which
workloads benefit under realistic costs and assumptions, not whether quantum
terminology makes an agent more intelligent.

There are three separate tracks:

1. **Knowledge about quantum science:** source-grounded papers, concepts and
   claims represented in the ordinary knowledge system.
2. **Quantum-assisted computation:** a classical agent proposes a bounded
   optimization/simulation job and interprets its measured results.
3. **Quantum-native agents:** deferred research about agents with persistent
   quantum resources or quantum communication. No architecture or benefit is assumed.

Multiple hypotheses in a report are classical records. They are not a physical
superposition. Agent agreement is not entanglement. Quantum results are evidence
under assumptions, never automatic truth or authorization.

## Reading and implementation path

- [Foundations and conceptual boundaries](FOUNDATIONS.md)
- [Hybrid architecture and adapter contracts](ARCHITECTURE.md)
- [Access: local simulators, IBM, Azure Quantum and Amazon Braket](ACCESS.md)
- [Experiments and quantum-advantage claim gates](EXPERIMENTS.md)
- [Annotated scientific sources](../research/READING_LIST.md)
- [Which source informs which design decision](../research/TRACEABILITY.md)

Begin with fundamentals, then reproduce a tiny local circuit experiment, then
compare a useful candidate workload against classical baselines. Remote hardware
is a later, explicitly authorized step. No cloud account or paid resource is
created by this documentation.
