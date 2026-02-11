from src.practice_01.core.basis_types import ExampleContext, ExamplePayload
from src.practice_01.extends.facade_workflow import ExampleFacade

if __name__ == "__main__":
    m_payload = ExamplePayload(
        data_loading = True,
        data_preprocessing = True,
        core_logic = True,
        data_postprocessing = True,
        result_analyze = True,
        result_merging = True,
        step_result_showcase_gen = True,
        final_result_showcase_gen = True,
        final_handover_data_gen = True,
        final_handover_showcase_gen = True,
    )

    m_context = ExampleContext(
        ## Constructor Init
        input__file__filepath = "data/raw/...",
        input__file__filename = "",
        output__file__filepath = "data/result/...",
        output__file__filename = "",
    )

    facade = ExampleFacade(
        payload=m_payload,
        context=m_context,
    )
    facade.workflow_execution()

