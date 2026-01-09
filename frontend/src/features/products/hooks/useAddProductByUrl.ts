import { useState } from "react";
import axios, { AxiosError } from "axios";

export function useAddProductByUrl() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState(false);

  const submit = async (url: string) => {
    try {
      setLoading(true);
      setError(null);
      setSuccess(false);

      await axios.post("/api/products/add-by-url", { url });
      setSuccess(true);
    } catch (err) {
      const error = err as AxiosError<{ message?: string }>;
      setError(error.response?.data?.message ?? "Failed to add product");
    } finally {
      setLoading(false);
    }
  };

  return { submit, loading, error, success };
}
