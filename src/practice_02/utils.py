from src.practice_02.core.base import IFacadeTask
from src.practice_02.core.basis_types import ExampleContext


class DataLoader(IFacadeTask):
    def run_task(self, context: ExampleContext, *args, **kwargs):
        print("\n>>> Running ``_data_loading`` !!!")
        print("\tDO SOMETHING")
        print("<<< ``_data_loading`` Successfully Exit !!!")

class DataPreprocessor(IFacadeTask):
    def run_task(self, context: ExampleContext, *args, **kwargs):
        print("\n>>> Running ``_data_preprocessing`` !!!")
        print("\tDO SOMETHING")
        print("<<< ``_data_preprocessing`` Successfully Exit !!!")

class CoreLogicRunner(IFacadeTask):
    def run_task(self, context: ExampleContext, *args, **kwargs):
        print("\n>>> Running ``_core_logic`` !!!")
        print("\tDO SOMETHING")
        print("<<< ``_core_logic`` Successfully Exit !!!")

class DataPostprocessor(IFacadeTask):
    def run_task(self, context: ExampleContext, *args, **kwargs):
        print("\n>>> Running ``_data_postprocessing`` !!!")
        print("\tDO SOMETHING")
        print("<<< ``_data_postprocessing`` Successfully Exit !!!")

class ResultAnalyzer(IFacadeTask):
    def run_task(self, context: ExampleContext, *args, **kwargs):
        print("\n>>> Running ``_result_analyze`` !!!")
        print("\tDO SOMETHING")
        print("<<< ``_result_analyze`` Successfully Exit !!!")

class ResultMerger(IFacadeTask):
    def run_task(self, context: ExampleContext, *args, **kwargs):
        print("\n>>> Running ``_result_merging`` !!!")
        print("\tDO SOMETHING")
        print("<<< ``_result_merging`` Successfully Exit !!!")

class StepResult_ShowcaseGen(IFacadeTask):
    def run_task(self, context: ExampleContext, *args, **kwargs):
        print("\n>>> Running ``_step_result_showcase_gen`` !!!")
        print("\tDO SOMETHING")
        print("<<< ``_step_result_showcase_gen`` Successfully Exit !!!")

class FinalResult_ShowcaseGen(IFacadeTask):
    def run_task(self, context: ExampleContext, *args, **kwargs):
        print("\n>>> Running ``_final_result_showcase_gen`` !!!")
        print("\tDO SOMETHING")
        print("<<< ``_final_result_showcase_gen`` Successfully Exit !!!")

class FinalHandover_DataGen(IFacadeTask):
    def run_task(self, context: ExampleContext, *args, **kwargs):
        print("\n>>> Running ``_final_handover_data_gen`` !!!")
        print("\tDO SOMETHING")
        print("<<< ``_final_handover_data_gen`` Successfully Exit !!!")

class FinalHandover_ShowcaseGen(IFacadeTask):
    def run_task(self, context: ExampleContext, *args, **kwargs):
        print("\n>>> Running ``_final_handover_showcase_gen`` !!!")
        print("\tDO SOMETHING")
        print("<<< ``_final_handover_showcase_gen`` Successfully Exit !!!")
