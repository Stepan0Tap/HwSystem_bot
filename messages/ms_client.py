# <---------- Основные сообщения ---------->
mscl_CommandStartOrHelp_WithGroup = (
	f'⚙️ [HomeWorker_Bot](https://t.me/HwSystem_bot)\n'
	f'Основные функции:\n'
	f' · Актуальные домашние задания\n'
	f'   /hw\n'
	f' · Актуальное расписание\n'
	f'   /schedule\n'
	f' · Предстоящие события\n'
	f'   /events\n'
	f' · Панель управления группой\n'
	f'   /group'
)


mscl_CommandStartOrHelp_NoGroup = (
	f'⚙️ [HomeWorker_Bot](https://t.me/HwSystem_bot)\n'
	f'Самое время войти в группу или создать её 👇'
)


def mscl_CommandStartOrHelp_NoRegister(first_name: str):
	return (
		f'⚙️ [HomeWorker_Bot](https://t.me/HwSystem_bot)\n'
		f'Привет, {first_name} 👋\n'
		f'Я помогу упорядочить твои знания\n'
		f'Начни со вступления в группу или её создания прямо сейчас 👇'
	)
