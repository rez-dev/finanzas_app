import { Link } from "react-router-dom";

export function Navigation() {
  return (
    <div>
      <Link to="/">
        <h1>Finance App</h1>
      </Link>
      <Link to="/users-create">create user</Link>
    </div>
  );
}
