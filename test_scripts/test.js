import http from "k6/http";
import { check, sleep } from "k6";

export default function () {
  const res = http.post("http://localhost:8000/execute", null, {
    headers: { "Content-Type": "application/json" },
  });
  check(res, {
    "status is 200": (r) => r.status === 200,
    "body ok": (r) => r.json("ok") === true,
  });

  sleep(1);
}
