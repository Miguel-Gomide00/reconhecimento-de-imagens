// app.js

const db = {
    get users() {
        return JSON.parse(localStorage.getItem('users')) || [];
    },
    set users(data) {
        localStorage.setItem('users', JSON.stringify(data));
    },
    get todos() {
        return JSON.parse(localStorage.getItem('todos')) || [];
    },
    set todos(data) {
        localStorage.setItem('todos', JSON.stringify(data));
    }
};

const session = {
    get currentUser() {
        return JSON.parse(localStorage.getItem('currentUser'));
    },
    login(user) {
        localStorage.setItem('currentUser', JSON.stringify(user));
    },
    logout() {
        localStorage.removeItem('currentUser');
    }
};

const screens = {
    login: document.getElementById('login-screen'),
    register: document.getElementById('register-screen'),
    todo: document.getElementById('todo-screen')
};

function showScreen(screenName) {
    Object.values(screens).forEach(screen => screen.classList.add('hidden-el'));
    screens[screenName].classList.remove('hidden-el');
}

function showError(elementId, message) {
    const el = document.getElementById(elementId);
    el.textContent = message;
    el.classList.remove('hidden-el');
}

function hideErrors() {
    document.querySelectorAll('[id$="-error"]').forEach(el => {
        el.classList.add('hidden-el');
        el.textContent = '';
    });
}

function init() {
    // CORREÇÃO PROBLEMA 2: A verificação session.currentUser busca do localStorage diretamente
    // Assim que a página for recarregada (quando o init rodar), a sessão salva é recuperada e o estado é mantido.
    const user = session.currentUser;
    if (user) {
        document.getElementById('welcome-message').textContent = `Olá, ${user.name}`;
        showScreen('todo');
        renderTasks();
    } else {
        showScreen('login');
    }
}

// Lógica de UI - Login e Registro
document.getElementById('show-register').addEventListener('click', () => {
    hideErrors();
    document.getElementById('login-form').reset();
    showScreen('register');
});

document.getElementById('show-login').addEventListener('click', () => {
    hideErrors();
    document.getElementById('register-form').reset();
    showScreen('login');
});

document.getElementById('logout-btn').addEventListener('click', () => {
    session.logout();
    showScreen('login');
});

// Processamento de Formulários
document.getElementById('login-form').addEventListener('submit', (e) => {
    e.preventDefault();
    hideErrors();

    const email = document.getElementById('login-email').value.trim();
    const password = document.getElementById('login-password').value.trim();
    
    let isValid = true;

    if (!email) {
        showError('login-email-error', 'O e-mail é obrigatório.');
        isValid = false;
    }
    
    if (!password) {
        showError('login-password-error', 'A senha é obrigatória.');
        isValid = false;
    }

    if (!isValid) return;

    const user = db.users.find(u => u.email === email && u.password === password);

    if (user) {
        session.login(user);
        document.getElementById('welcome-message').textContent = `Olá, ${user.name}`;
        document.getElementById('login-form').reset();
        showScreen('todo');
        renderTasks();
    } else {
        showError('login-general-error', 'E-mail não cadastrado ou senha incorreta.');
    }
});

document.getElementById('register-form').addEventListener('submit', (e) => {
    e.preventDefault();
    hideErrors();

    const name = document.getElementById('register-name').value.trim();
    const email = document.getElementById('register-email').value.trim();
    const password = document.getElementById('register-password').value.trim();
    
    let isValid = true;

    if (!name) {
        showError('register-name-error', 'O nome é obrigatório.');
        isValid = false;
    }

    if (!email) {
        showError('register-email-error', 'O e-mail é obrigatório.');
        isValid = false;
    }
    
    if (!password) {
        showError('register-password-error', 'A senha é obrigatória.');
        isValid = false;
    }

    if (!isValid) return;

    const users = db.users;
    if (users.find(u => u.email === email)) {
        showError('register-general-error', 'Este e-mail já está cadastrado.');
        return;
    }

    const newUser = { id: Date.now().toString(), name, email, password };
    users.push(newUser);
    db.users = users;

    session.login(newUser);
    document.getElementById('welcome-message').textContent = `Olá, ${newUser.name}`;
    document.getElementById('register-form').reset();
    showScreen('todo');
    renderTasks();
});

// Lógica de Tarefas
document.getElementById('task-form').addEventListener('submit', (e) => {
    e.preventDefault();
    hideErrors(); // Limpa erros anteriores no form

    const title = document.getElementById('task-title').value.trim();
    const type = document.getElementById('task-type').value;
    const description = document.getElementById('task-desc').value.trim();
    const user = session.currentUser;
    
    // CORREÇÃO PROBLEMA 3: Validação adicionada para rejeitar título vazio (mesmo
    // com o atributo "required" no HTML, scripts não devem confiar só nisso)
    if (!title) {
        showError('task-title-error', 'O título da tarefa é obrigatório e não pode ser apenas espaços.');
        return;
    }

    if (!user) return;
    
    const newTask = {
        id: Date.now(),
        userId: user.email,
        title,
        type,
        description,
        done: false
    };
    
    const todos = db.todos;
    todos.push(newTask);
    db.todos = todos;
    
    document.getElementById('task-form').reset();
    renderTasks();
});

window.completeTask = function(taskId) {
    const todos = db.todos;
    const taskIndex = todos.findIndex(t => t.id === taskId);
    
    if (taskIndex !== -1) {
        // CORREÇÃO PROBLEMA 1: A tarefa NÃO é removida do array de banco de dados. 
        // Em vez disso, a propriedade 'done' é atualizada para true, e ao renderizar,
        // a classe "line-through" a exibe riscada, posicionando-a automaticamente no fim da lista.
        todos[taskIndex].done = true;
        db.todos = todos;
        renderTasks();
    }
};

function renderTasks() {
    const container = document.getElementById('tasks-container');
    const noTasksMsg = document.getElementById('no-tasks-message');
    const user = session.currentUser;
    
    if (!user) return;
    
    container.innerHTML = '';
    
    const userTasks = db.todos.filter(t => t.userId === user.email);
    
    if (userTasks.length === 0) {
        noTasksMsg.classList.remove('hidden-el');
        return;
    }
    
    noTasksMsg.classList.add('hidden-el');
    
    userTasks.sort((a, b) => {
        if (a.done === b.done) return b.id - a.id; 
        return a.done ? 1 : -1;
    });
    
    const badgeColors = {
        'Trabalho': 'bg-blue-500/20 text-blue-400 border-blue-500/30',
        'Pessoal': 'bg-purple-500/20 text-purple-400 border-purple-500/30',
        'Estudos': 'bg-green-500/20 text-green-400 border-green-500/30'
    };

    userTasks.forEach(task => {
        const badgeClass = badgeColors[task.type] || 'bg-slate-500/20 text-slate-400 border-slate-500/30';
        const cardOpacity = task.done ? 'opacity-50' : 'opacity-100';
        const titleStyle = task.done ? 'line-through text-slate-500' : 'text-white';
        
        const card = document.createElement('div');
        card.className = `bg-slate-800/40 border ${task.done ? 'border-slate-800' : 'border-slate-700/50'} rounded-xl p-5 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 transition-all hover:bg-slate-800/60 ${cardOpacity}`;
        
        card.innerHTML = `
            <div class="flex-1 w-full break-words">
                <div class="flex items-center gap-3 mb-1 flex-wrap">
                    <h3 class="font-semibold text-lg ${titleStyle}">${task.title}</h3>
                    <span class="text-xs px-2.5 py-1 rounded-full border whitespace-nowrap ${badgeClass}">${task.type}</span>
                </div>
                ${task.description ? `<p class="text-slate-400 text-sm mt-2 whitespace-pre-wrap">${task.description}</p>` : ''}
            </div>
            ${!task.done ? `
                <button onclick="completeTask(${task.id})" class="shrink-0 bg-emerald-500/10 hover:bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 font-medium py-1.5 px-4 rounded-lg transition-colors text-sm w-full sm:w-auto">
                    Concluir
                </button>
            ` : `
                <span class="shrink-0 text-slate-500 text-sm font-medium px-4 py-1.5 w-full sm:w-auto text-left sm:text-right">Concluída</span>
            `}
        `;
        container.appendChild(card);
    });
}

// Iniciar
init();
