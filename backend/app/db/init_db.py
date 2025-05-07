import logging
from sqlalchemy.orm import Session

from app.db.base import Base, engine
from app.models.base import User, Content, PerformanceMetric, SystemConfig

logger = logging.getLogger(__name__)

def init_db() -> None:
    """
    Initialize the database by creating all tables and adding initial data.
    """
    try:
        # Create all tables
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Error creating database tables: {e}")
        raise

def create_initial_data(db: Session) -> None:
    """
    Create initial system configuration data.
    """
    try:
        # Check if we already have system configs
        if db.query(SystemConfig).first() is None:
            # Create default system configurations
            default_configs = [
                SystemConfig(
                    key="content_types",
                    value=["post", "story", "reel"],
                    description="Available content types for the platform"
                ),
                SystemConfig(
                    key="platforms",
                    value=["instagram", "tiktok"],
                    description="Supported social media platforms"
                ),
                SystemConfig(
                    key="content_statuses",
                    value=["draft", "scheduled", "published", "archived"],
                    description="Possible content statuses"
                ),
                SystemConfig(
                    key="metric_types",
                    value=["likes", "comments", "shares", "reach", "engagement_rate"],
                    description="Types of performance metrics tracked"
                )
            ]
            
            db.add_all(default_configs)
            db.commit()
            logger.info("Initial system configurations created successfully")
    except Exception as e:
        logger.error(f"Error creating initial data: {e}")
        db.rollback()
        raise 