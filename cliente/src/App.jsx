import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom';
import {UsersPage} from './pages/UsersPage';
import {UserFormPage} from './pages/UserFormPage';
import {Navigation} from './components/Navigation';

function App(){
  return (
    <BrowserRouter>
      <Navigation/>
      <Routes>
        <Route path='/' element={<Navigate to='/users' />} />
        <Route path='/users' element={<UsersPage/>} />
        <Route path='/users-create' element={<UserFormPage/>} />
      </Routes>
    </BrowserRouter>
  )
}

export default App;