from src.practice_01.core.base import IMainFacade
from src.practice_01.core.basis_types import ExamplePayload, ExampleContext, ExampleStep


class ExampleFacade(IMainFacade):
    def __init__(self, payload: ExamplePayload, context: ExampleContext):
        super().__init__(payload, context)

    def workflow_execution(self, *args, **kwargs):
        if self._payload[ExampleStep.DATA_LOADING.value]:
            self._data_loading()
        if self._payload[ExampleStep.DATA_PREPROCESSING.value]:
            self._data_preprocessing()
        if self._payload[ExampleStep.CORE_LOGIC.value]:
            self._core_logic()
        if self._payload[ExampleStep.DATA_POSTPROCESSING.value]:
            self._data_postprocessing()
        if self._payload[ExampleStep.RESULT_ANALYZE.value]:
            self._result_analyze()
        if self._payload[ExampleStep.RESULT_MERGING.value]:
            self._result_merging()
        if self._payload[ExampleStep.STEP_RESULT_SHOWCASE_GEN.value]:
            self._step_result_showcase_gen()
        if self._payload[ExampleStep.FINAL_RESULT_SHOWCASE_GEN.value]:
            self._final_result_showcase_gen()
        if self._payload[ExampleStep.FINAL_HANDOVER_DATA_GEN.value]:
            self._final_handover_data_gen()
        if self._payload[ExampleStep.FINAL_HANDOVER_SHOWCASE_GEN.value]:
            self._final_handover_showcase_gen()

    def _data_loading(self):
        print("\n>>> Running ``_data_loading`` !!!")
        context = self._context
        print("<<< ``_data_loading`` Successfully Exit !!!")
        pass

    def _data_preprocessing(self):
        print("\n>>> Running ``_data_preprocessing`` !!!")
        context = self._context
        print("<<< ``_data_preprocessing`` Successfully Exit !!!")
        pass

    def _core_logic(self):
        print("\n>>> Running ``_core_logic`` !!!")
        context = self._context
        print("<<< ``_core_logic`` Successfully Exit !!!")
        pass

    def _data_postprocessing(self):
        print("\n>>> Running ``_data_postprocessing`` !!!")
        context = self._context
        print("<<< ``_data_postprocessing`` Successfully Exit !!!")
        pass

    def _result_analyze(self):
        print("\n>>> Running ``_result_analyze`` !!!")
        context = self._context
        print("<<< ``_result_analyze`` Successfully Exit !!!")
        pass

    def _result_merging(self):
        print("\n>>> Running ``_result_merging`` !!!")
        context = self._context
        print("<<< ``_result_merging`` Successfully Exit !!!")
        pass

    def _step_result_showcase_gen(self):
        print("\n>>> Running ``_step_result_showcase_gen`` !!!")
        context = self._context
        print("<<< ``_step_result_showcase_gen`` Successfully Exit !!!")
        pass

    def _final_result_showcase_gen(self):
        print("\n>>> Running ``_final_result_showcase_gen`` !!!")
        context = self._context
        print("<<< ``_final_result_showcase_gen`` Successfully Exit !!!")
        pass

    def _final_handover_data_gen(self):
        print("\n>>> Running ``_final_handover_data_gen`` !!!")
        context = self._context
        print("<<< ``_final_handover_data_gen`` Successfully Exit !!!")
        pass

    def _final_handover_showcase_gen(self):
        print("\n>>> Running ``_final_handover_showcase_gen`` !!!")
        context = self._context
        print("<<< ``_final_handover_showcase_gen`` Successfully Exit !!!")
        pass
