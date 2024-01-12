export function UserCard({ user }) {
  return (
    <div>
      <h3>{user.name}</h3>
      <p>{user.email}</p>
      <p>{user.password}</p>
      <hr />
    </div>
  );
}
