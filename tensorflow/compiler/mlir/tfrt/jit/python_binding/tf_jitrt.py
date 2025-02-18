# Copyright 2021 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Minimal Python binding for Tensorflow CPURT JIT compilation.

This is only for testing Tensorflow CPURT compilation pipeline.
"""

from tensorflow.compiler.mlir.tfrt.jit.python_binding import _tf_jitrt_executor


class TfCpurtExecutor(_tf_jitrt_executor.TfCpurtExecutor):
  """Python binding of `tensorflow::TfCpurtExecutor` class."""

class Specialization(_tf_jitrt_executor.Specialization):
  """Python binding of `tensorflow::TfCpurtExecutor::Specialization` enum."""
