import { UserRole } from '@/store/authStore'

interface RoleBadgeProps {
  role: UserRole
}

const roleConfig = {
  admin: { label: 'Admin', color: 'bg-purple-100 text-purple-700' },
  ca: { label: 'CA', color: 'bg-blue-100 text-blue-700' },
  client: { label: 'Client', color: 'bg-green-100 text-green-700' },
  auditor: { label: 'Auditor', color: 'bg-orange-100 text-orange-700' },
}

export default function RoleBadge({ role }: RoleBadgeProps) {
  const config = roleConfig[role]

  return (
    <span className={`inline-block px-2 py-0.5 rounded-full text-xs font-medium ${config.color}`}>
      {config.label}
    </span>
  )
}
