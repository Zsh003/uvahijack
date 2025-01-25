// src/utils/types.ts


/**
 * 通用 API 响应结构
 */
export interface ApiResponse<T> {
  data: T;
  status: number;
  statusText: string;
}

/**
 * 启动劫持接口的请求参数
 */
export interface ReplayHijackParams {
  deviceIp: string; // 设备 IP
  port: number; // 端口号
}