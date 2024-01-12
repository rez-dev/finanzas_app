import { useForm } from "react-hook-form";
import { createUser } from "../api/users.api";
import { useNavigate } from "react-router-dom";
export function UserFormPage() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmit = handleSubmit(async (data) => {
    // console.log(data);
    const respuesta = await createUser(data);
    console.log(respuesta);
    navigate("/users");
  });

  const navigate = useNavigate();

  return (
    <div>
      <form onSubmit={onSubmit}>
        <input
          type="text"
          placeholder="name"
          {...register("name", { required: true })}
        />
        {errors.name && <span>name is required</span>}
        <input
          type="email"
          placeholder="email"
          {...register("email", { required: true })}
        />
        {errors.email && <span>email is required</span>}
        <input
          type="password"
          placeholder="password"
          {...register("password", { required: true })}
        />
        {errors.password && <span>password is required</span>}
        <button type="submit">submit</button>
      </form>
    </div>
  );
}
