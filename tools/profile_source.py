"""Static source-performance profiler based on Python AST."""
import ast
from contracts.tool_contract import ToolContract, ToolMetadata


def _profile(inputs: dict) -> dict:
    source = inputs["source"]
    tree = ast.parse(source)
    loops = sum(isinstance(n, (ast.For, ast.While, ast.AsyncFor)) for n in ast.walk(tree))
    calls = sum(isinstance(n, ast.Call) for n in ast.walk(tree))
    comprehensions = sum(isinstance(n, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)) for n in ast.walk(tree))
    functions = [n.name for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
    return {"metrics": {"loop_count": loops, "call_count": calls, "comprehension_count": comprehensions, "function_count": len(functions)}, "functions": functions}


TOOL = ToolContract(ToolMetadata("profile_source", "Extract deterministic static performance indicators from Python source.", {"type": "object", "properties": {"source": {"type": "string", "minLength": 1}}, "required": ["source"], "additionalProperties": False}), _profile)
