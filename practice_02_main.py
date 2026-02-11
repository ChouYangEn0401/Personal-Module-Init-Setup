from src.practice_02.core.base import IPayload
from src.practice_02.core.basis_types import ExamplePayload, ExampleStep
from src.practice_02.extends.facade_workflow import example_facade
from src.practice_02.utils import *


EventBindings = {
    ExampleStep.DATA_LOADING.value: DataLoader,
    ExampleStep.DATA_PREPROCESSING.value: DataPreprocessor,
    ExampleStep.CORE_LOGIC.value: CoreLogicRunner,
    ExampleStep.DATA_POSTPROCESSING.value: DataPostprocessor,
    ExampleStep.RESULT_ANALYZE.value: ResultAnalyzer,
    ExampleStep.RESULT_MERGING.value: ResultMerger,
    ExampleStep.FINAL_HANDOVER_DATA_GEN.value: FinalHandover_DataGen,
    ExampleStep.FINAL_RESULT_SHOWCASE_GEN.value: FinalResult_ShowcaseGen,
    ExampleStep.FINAL_HANDOVER_SHOWCASE_GEN.value: FinalHandover_ShowcaseGen,
}

# ### TODO: 可以把我刪掉 ###
def 補充ENUM其他用法():
    from src.practice_02.core.base import PayloadBase, IPayload

    # 寫法 1：明確標註型別
    payload1: ExamplePayload = {
        ExampleStep.DATA_LOADING: True,
        ExampleStep.CORE_LOGIC: False,
    }

    # 寫法 2：如果不使用繼承後的 ExamplePayload，直接用泛型
    payload2: IPayload[ExampleStep] = {
        ExampleStep.DATA_PREPROCESSING: True
    }
    # 假設使用 PayloadBase 邏輯
    payload3 = PayloadBase[ExampleStep]()
    payload3[ExampleStep.DATA_LOADING] = True

    return payload1, payload2, payload3
# ### TODO: 可以把我刪掉 ###


if __name__ == "__main__":
    ## [最推薦] 物件宣告法，用arg設定dictionary
    m_payload = ExamplePayload(
        # data_loading = False,
        data_preprocessing = False,
        core_logic = False,
        data_postprocessing = False,
        result_analyze = False,
        result_merging = False,
        final_result_showcase_gen = True,
        final_handover_data_gen = True,
        final_handover_showcase_gen = False,
    )

    # ### TODO: 可以把我刪掉 ###

    ## 直接設定某參數: 但順序會壞掉(如果一開始沒有init)，重視順序就不可如此
    m_payload[ExampleStep.FINAL_HANDOVER_SHOWCASE_GEN.value] = True
    m_payload[ExampleStep.DATA_LOADING] = True
    ## 直接傳送整個dictionary
    m_payload: IPayload[ExampleStep] = {
        ExampleStep.RESULT_ANALYZE: True,
        ExampleStep.RESULT_MERGING.value: True,
    }

    # ### TODO: 可以把我刪掉 ###


    m_context = ExampleContext(
        ## Constructor Init
        input__file__filepath = "data/raw/...",
        input__file__filename = "",
        output__file__filepath = "data/result/...",
        output__file__filename = "",
    )

    example_facade(
        payload=m_payload,  ## 目前寫好了只接受`ExamplePayload`
        EventBindings=EventBindings,
        context=m_context,
    )

