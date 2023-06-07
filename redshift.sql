drop table public.shoes

CREATE TABLE public.shoes (
  type VARCHAR(50) NOT NULL,
  color VARCHAR(50) NOT NULL
);

INSERT INTO public.shoes (type, color)
VALUES
  ('loafera', 'brown'),
  ('sandals', 'black');