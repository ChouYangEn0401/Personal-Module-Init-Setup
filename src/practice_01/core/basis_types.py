from dataclasses import dataclass

from src.practice_01.core.base import IPayload, IContext, IStepEnum


class ExampleStep(IStepEnum):
    DATA_LOADING = "data_loading"
    DATA_PREPROCESSING = "data_preprocessing"
    CORE_LOGIC = "core_logic"
    DATA_POSTPROCESSING = "data_postprocessing"
    RESULT_ANALYZE = "result_analyze"
    RESULT_MERGING = "result_merging"
    STEP_RESULT_SHOWCASE_GEN = "step_result_showcase_gen"
    FINAL_RESULT_SHOWCASE_GEN = "final_result_showcase_gen"
    FINAL_HANDOVER_DATA_GEN = "final_handover_data_gen"
    FINAL_HANDOVER_SHOWCASE_GEN = "final_handover_showcase_gen"

class ExamplePayload(IPayload):
    ## reading file from `data/raw`
    data_loading: bool

    ## saving file into `data/processed`
    data_preprocessing: bool
    ## saving file into `data/result`
    core_logic: bool
    ## saving file into `data/processed`
    data_postprocessing: bool

    ## loading and saving file into `data/result`
    result_analyze: bool
    result_merging: bool

    step_result_showcase_gen: bool
    final_result_showcase_gen: bool

    ## saving file into `data/final`
    final_handover_data_gen: bool
    final_handover_showcase_gen: bool


@dataclass
class ExampleContext(IContext):
    ## Constructor Init
    input__file__filepath: str
    input__file__filename: str
    output__file__filepath: str
    output__file__filename: str

    ## Lazy Init
    runtime_config = None




