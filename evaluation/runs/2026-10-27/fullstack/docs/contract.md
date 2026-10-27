# 当前数据与接口约定

每个设备包含字符串 id 和 name；JSON 文件为设备数组。GET /api/items 返回 {"items": [...]}。本次增加 POST /api/items，接收 {"name": "设备名"}，非空白名称成功后追加设备并返回 201 与 {"item": {...}}；空白名称返回 400 与 {"error": "name_required"}，保留已有数据。id 由服务端产生，名称去除首尾空白。

缺失名称或非字符串名称同样返回 400 与 {"error": "name_required"}。请求体不是有效 JSON 时返回 400 与 {"error": "invalid_json"}。数据读取或保存失败时返回 500 与 {"error": "storage_error"}；新增采用加锁的读写和临时文件替换，失败时保留原数据。
